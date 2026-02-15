---
title: Integrate Dynatrace Lambda Layer on container images
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images
scraped: 2026-02-15T09:14:03.761535
---

# Integrate Dynatrace Lambda Layer on container images

# Integrate Dynatrace Lambda Layer on container images

* How-to guide
* 4-min read
* Updated on Jan 22, 2026

As an addition to Lambda function deployment as a ZIP file, AWS Lambda offers [Lambda function deployment as container imagesï»¿](https://aws.amazon.com/de/blogs/aws/new-for-aws-lambda-container-image-support/).

The container image must include the files and configuration required to run the function code. The same applies to the files and configuration of Dynatrace AWS Lambda Layer, once monitoring is enabled for the containerized Lambda function.

In a ZIP file function deployment, the Dynatrace artifacts are attached to the function with an [AWS Lambda extensionï»¿](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html) (which is a Lambda layer with an extension-specific folder layout).

A Lambda layer, like a function bundle, is a ZIP file extracted at function cold start time to the `/opt` folder of the AWS Lambda function instance.

See below for how to enable Dynatrace monitoring for a containerized Lambda function.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Configuration**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images#configuration "Deploy Dynatrace Lambda Layers when deployed via a container image.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Copy the Lambda layer configuration snippet**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images#copy-layer-snippet "Deploy Dynatrace Lambda Layers when deployed via a container image.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Add Dynatrace AWS Lambda extension to the container image**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images#add-oneagent-extension "Deploy Dynatrace Lambda Layers when deployed via a container image.")

## Step 1 Configuration

1. Go to [Trace Python, Node.js, and Java Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") and follow the **Configure with environment variables** instructions.
2. Open the projects `Dockerfile` in an editor and copy the environment variables from the deployment screen. Each
   line must be prefixed with `ENV` and spaces around the equal signs must be removed.

```
ENV AWS_LAMBDA_EXEC_WRAPPER=/opt/dynatrace



ENV DT_TENANT=abcd1234



ENV DT_CLUSTER_ID=1234567890



ENV DT_CONNECTION_BASE_URL=https://abcd1234.live.dynatrace.com



ENV DT_CONNECTION_AUTH_TOKEN=dt0a01...
```

## Step 2 Copy the Lambda layer configuration snippet

1. In Dynatrace Hub, select **AWS Lambda**.
2. Select **Set up**.

3. On the **Enable Monitoring for AWS Lambda Functions**, copy the Lambda layer configuration snippet.

## Step 3 Add OneAgent extension to the container image

1. To download the contents of the Dynatrace AWS Lambda extension to the local file system, use the following code sample for [dt-awslayertool](#dt-awslayertool) or [AWS CLI](#aws-cli).

   Via dt-awslayertool

   Via AWS CLI

   To use the following code sample, substitute `<YOUR_LAMBDA_LAYER_ARN_SNIPPET>` with the [copied Lambda layer snippet](#copy-layer-snippet).

   ```
   dt-awslayertool pull <YOUR_LAMBDA_LAYER_ARN_SNIPPET> --extract DynatraceOneAgentExtension
   ```

   Example command

   The following example command downloads the layer `arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1` and extracts its contents to the local folder `DynatraceOneAgentExtension`.

   ```
   dt-awslayertool pull arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1 --extract DynatraceOneAgentExtension
   ```

   To learn more about dt-awslayertool, see [Githubï»¿](https://github.com/dynatrace-oss/dt-awslayertool).

   To use the following code sample, substitute `<YOUR_LAMBDA_LAYER_ARN_SNIPPET>` with the [copied Lambda layer snippet](#copy-layer-snippet) and `<YOUR_LAMBDA_LAYER_REGION>`  with the Lambda layer region provided in the snippet.

   ```
   curl $(aws --region <YOUR_LAMBDA_LAYER_REGION> lambda get-layer-version-by-arn --arn <YOUR_LAMBDA_LAYER_ARN_SNIPPET> --query 'Content.Location' --output text) --output layer.zip



   unzip -d DynatraceOneAgentExtension layer.zip
   ```

   Example command

   The following code example downloads and extracts the content of `arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1` to the local folder `DynatraceOneAgentExtension`.

   ```
   curl $(aws --region us-east-1 lambda get-layer-version-by-arn --arn arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1 --query 'Content.Location' --output text) --output layer.zip



   unzip -d DynatraceOneAgentExtension layer.zip
   ```

   To learn more about AWS CLI, see [AWS documentationï»¿](https://docs.aws.amazon.com/cli/index.html).
2. To copy the downloaded extension content into the container image and ensure that the shell script file `/opt/dynatrace` is executable, use the following `Dockerfile` commands.

   ```
   COPY DynatraceOneAgentExtension/ /opt/



   RUN chmod +x /opt/dynatrace
   ```

### Sample `Dockerfile` with Dynatrace AWS Lambda extension enabled

This sample project creates a containerized Node.js Lambda function.

The project folder has the following files and folders:

```
containerized-lambda-sample



âââ Dockerfile



âââ DynatraceOneAgentExtension



âââ index.js
```

The content of the Dynatrace AWS Lambda Layer is assumed to be downloaded and extracted (as outlined above) to the folder `DynatraceOneAgentExtension`.

The handler function is exported by the `index.js` file:

```
exports.handler = async () => {



return "hello world";



}
```

The `Dockerfile` with the modifications applied to integrate Dynatrace AWS Lambda extension to the containerized function:

```
FROM public.ecr.aws/lambda/nodejs:18



COPY index.js ${LAMBDA_TASK_ROOT}



# --- Begin of enable Dynatrace OneAgent monitoring section



# environment variables copied from Dynatrace AWS Lambda deployment screen



# (prefix with ENV and remove spaces around equal signs)



ENV AWS_LAMBDA_EXEC_WRAPPER=/opt/dynatrace



ENV DT_TENANT=abcd1234



ENV DT_CLUSTER_ID=1234567890



ENV DT_CONNECTION_BASE_URL=https://abcd1234.live.dynatrace.com



ENV DT_CONNECTION_AUTH_TOKEN=dt0a01...



# copy Dynatrace OneAgent extension download and extracted to local disk into container image



COPY DynatraceOneAgentExtension/ /opt/



# make /opt/dynatrace shell script executable



RUN chmod +x /opt/dynatrace



# --- End of enable Dynatrace OneAgent monitoring section



CMD [ "index.handler" ]
```

## Limitations

Monitoring via Dynatrace AWS Lambda extension on container images is supported only for images [created from an AWS base image for Lambdaï»¿](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-1) and only for [the runtimes that we support for non-containerized functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "AWS Lambda capabilities and integration options").

## Additional resources

For more information on the Lambda container images, see:

* [Creating Lambda container imagesï»¿](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
* [Working with Lambda layers and extensions in container imagesï»¿](https://aws.amazon.com/de/blogs/compute/working-with-lambda-layers-and-extensions-in-container-images/)