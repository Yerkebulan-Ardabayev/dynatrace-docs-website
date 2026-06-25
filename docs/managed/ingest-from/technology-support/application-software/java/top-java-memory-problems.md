---
title: Top Java memory problems
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/top-java-memory-problems
scraped: 2026-05-12T12:04:30.165098
---

# Top Java memory problems

# Top Java memory problems

* 15-min read
* Published Mar 29, 2019

This topic explains frequently occurring memory issues, such as memory leaks, high memory usage, class loader problems, and GC configuration.

## Memory leaks

The most common memory leak issue is growing memory leaks, or the constant rise of leaked objects. These leaks can be easily tracked down through trending or histogram dumps.

In comparison, single object leaks are less talked about. As long as there is enough memory, single memory leaks seldom pose a significant problem. However, from time to time, single object leaks occupy a considerable amount of memory and pose a problem. The good news is that single big leaks can be easily identified by heap analyzer tools.

The following are some of the causes of memory leaks:

Thread local variables

`ThreadLocal` variables are used to bind a variable or a state to a thread. Each thread has its own instance of the variable. While `ThreadLocal` variables can be useful, they can also be dangerous. They are used to track a state, such as the current transaction ID, but sometimes hold some more information.

A `ThreadLocal` variable is referenced by its thread and its lifecycle is bound to it. In most application servers, threads are reused via thread pools and are never garbage collected. If the application code does not carefully clear the `ThreadLocal` variable, it results in a nasty memory leak. Such leaks can be easily discovered with a heap dump by looking at the `ThreadLocalMap` and following the references.

In the above screen, the heapdump indicates that over 4K objects, which amount to around 10MB in size, are held by `ThreadLocal` variables. The name of the thread reveals the part of the application that is responsible for the leak.

Mutable static fields and collections

The most common reason for a memory leak is the wrong usage of statics. A static variable is held by its class and, subsequently, by its classloader. While a class can be garbage collected, it will seldom happen during an application's lifetime. Often, statics are used to hold cache information or share state across threads. If this is not done diligently, it is easy to get a memory leak. For this reason, static mutable collections must be avoided at all costs. A good architectural rule is to not use mutable static objects at all and settle for better alternatives.

Circular and complex bi-directional references

Consider the following example:

```
org.w3c.dom.Document doc = readXmlDocument();



org.w3c.dom.Node child = doc.getDocumentElement().getFirstChild();



doc.removeNode(child);



doc = null;
```

At the end of the snippet, the assumption is that DOM Document will be garbage collected. However, that is not the case. A DOM Node object always belongs to Document. Even when removed from Document, the Node object refers to its owning document. As long as the child object is kept, Document and all the nodes it contains are not garbage collected.

JNI memory leaks

JNI is used to call the native code from Java. This native code can handle, call, and create Java objects. Every Java object created by the native method begins its life as a `local reference`, which means that the object is referenced until the native method returns. The native method references the Java object, so there's no problem unless the native method runs forever. In some cases, you might want to keep the created object even after the native call has ended. To achieve this, you can either ensure that it is referenced by some other Java object or you can change the `local reference` to a `global reference`. A global reference is a GC root and will never be garbage collected until explicitly deleted by the native code. The only way to discover such a memory leak is to use a heap dump tool that explicitly shows global native references. If you have to use JNI, you should ensure that you reference these objects normally and forgo global references altogether.

You can find this sort of leak when your heap dump analysis tool explicitly marks the GC Root as a native reference, otherwise you will have a hard time.

Wrong implementation of equals/hashcode

If equals/hashcode methods violate the equals contract, it leads to memory leaks when used as a key in a map. A HashMap uses the hashcode to look up an object and verify that it found it by using the equals method. If two objects are equal they must have the same hashcode, but not the other way around. This is not the case when you do not explicitly implement the hashcode. The default hashcode is based on object identity. Therefore, by using an object without a valid hashcode implementation as a key in a map, you can add things but you won't be able to find them anymore. If you choose to re-add it, it won't overwrite the old item but add a new one, resulting in a memory leak. You will find it as it grows, but the root cause is hard to determine unless you remember this one.

The easiest way to avoid such a leak is to use unit testcases and one of the available frameworks that tests the equals contract of your classes.

Classloader leaks

Classloader leaks are found in application servers and OSGi containers. Classes are referenced by their classloader and are normally not garbage collected until the classloader itself is collected. However, this happens only when the application gets unloaded by the application server or OSGi container. The following are two forms of classloader leaks:

* The first form is that of an object whose class belongs to the class loader is still referenced by a cache, a local thread, or by some other means. In this case, the whole class loader, which is the whole application, can't be garbage collected. This happens in OSGi containers and JEE application servers. These memory leaks are not too frequent because they happen only when the application is unloaded or redeployed.
* The second form was introduced by bytecode manipulation frameworks such as BCEL and ASM. These frameworks allow the dynamic creation of new classes. When classes are left forgotten, the responsible code might create new classes for the same purpose multiple times. The class is referenced in the current class loader, which is why you can end up with a memory leak that can lead to an out-of-memory situation in the permanent generation. Most heap analyzer tools do not point out this problem, so it has to be analyzed manually. This form of memory leak is famous because of an issue in an older version of hibernate and its usage of CGLIB.

## High memory usage

Too much memory usage is an increasingly frequent and critical problem in todayâs enterprise applications. Although the average server often has 10, 20, or more GB of memory, a high degree of parallelism and a lack of awareness lead to memory shortages. Another issue is that while it is possible to use multiple gigabytes of memory in todayâs JVMs, the side effects a very long GC pauses. In some cases, increasing the memory can be a workaround to memory leaks or badly written software. However, more often than not, this makes things worse in the long run and not better. The following are the most common causes of high memory usage:

HTTP session as cache

The session caching anti-pattern refers to the misuse of the HTTP session as data cache. The HTTP session is used to store user data or the state that needs to survive a single HTTP request. This is referred to as the conversational state and is found in web applications that deal with non-trivial user interactions. The HTTP session has several problems.

First, as there can be a large number of users, a single web server can have quite a lot of active sessions. Therefore, it is important to keep them small. The second problem is that they are not specifically released by the application at a given point in time. Instead, web servers have a session timeout which is often quite high to increase user comfort. This alone can easily lead to large memory demands if the number of parallel users is considered. However, in reality, HTTP sessions are usually several megabytes in size.

These caches happen because it is easy and convenient for the developer to simply add objects to the session instead of thinking of other solutions like a cache. This is often done in a fire-and-forget mode, meaning that data is never removed.

An example of this is the storage of data that is displayed in HTML selection fields, such as country lists. This semi-static data is often multiple kilobytes in size and is held per user in the heap if kept in the session. It is better to store this in one central cache. Another example is the misuse of the hibernate session to manage the conversational state. The hibernate session is stored in the HTTP session in order to facilitate quick access to the data. This means storage of far more states than required, and with only a couple of users, memory usage immediately increases greatly. In modern Ajax applications, it is possible to shift the conversational state to the client. In the ideal case, this leads to a state-less or state-poor server application that scales much better.

Replication of long HTTP sessions is also another problem.

Wrong cache usage

Caches are used to increase performance and scalability by loading data only once. However, excessive use of caches can quickly lead to Java performance problems. In addition to the typical cache problems such as misses and high turnaround, a cache can also lead to high memory usage and excessive GC behavior. These problems are usually due to an excessively large cache. However, sometimes the problem lies someplace deeper.

A soft reference is a special form of object reference. While soft references can be released at any time at the discretion of the garbage collector, they are actually released only to avoid an out-of-memory error. In this respect, they differ greatly from weak references, which never prevent the garbage collection of an object. Soft references are therefore very popular in cache implementations.

The cache developer correctly assumes that the cache data is to be released in the event of a memory shortage. If the cache is incorrectly configured, it will grow quickly and indefinitely until the memory is full. When a GC is initiated, all soft references in the cache are cleared and their objects garbage collected. The memory usage drops back to the base level, only to start growing again. This phenomenon can easily be mistaken to be an incorrectly configured young generation. It looks like the objects are tenured too early only to be collected by the next major GC. This kind of problem often leads to a GC tuning exercise that canât succeed.

Only proper monitoring of the cache metrics or a heap dump can help identify the root cause of the problem.

Churn rate and high transactional memory usage

The generational GC is designed for a large number of very short-lived objects. If the transactional memory usage is too high, it can quickly lead to performance or stability problems. However, this type of problem is observed only during a load test and can be overlooked very easily during development.

If too many objects are created in too short a time, it leads to an increased number of GCs in the young generation, which are only cheap if most objects die. If a lot of objects survive the GC, it is actually more expensive than an old generation GC would be under similar circumstances. High memory needs of single transactions therefore might not be a problem in a functional test but can quickly lead to GC thrashing under load. If the load becomes even higher, these transactional objects are promoted to the old generation as the young generation becomes too small. if the size of the young generation is increased, it would push the problem out but ultimately lead to even longer GC pauses.

An out-of-memory error due to high transactional memory demand is the worst possible scenario. If memory is already tight, higher transaction load might simply max out the available heap. The tricky part is that once OutOfMemory hits, transactions that wanted to allocate objects but couldnât are aborted. Subsequently, a lot of memory is released and garbage is collected. As most memory tools only look at the Java memory every couple of seconds, they might not even show 100% memory at any point in time.

Since Java 6 it is possible to trigger a heap dump in the event of an OutOfMemory which will show the root cause. If there is no OutOfMemory, trending or histo memory dumps can be used to identify the classes whose object numbers fluctuate the most, usually those that are allotted and garbage-collected a lot. The last resort is to perform a full-scale allocation analysis.

Large temporary objects

Temporary objects also cause out-of-memory errors or increased GC activity. This happens when large documents have to be read and processed.

```
byte tmpData[] = new byte[1024];



int offs = 0;



do



{



int readLen = bis.read(tmpData, offs, tmpData.length - offs);



if(readLen == -1)



break;



offs += readLen;



if(offs == tmpData.length) {



byte newres[] = new byte[tmpData.length + 1024];



System.arraycopy(tmpData, 0, newres, 0,tmpData.length);



tmpData = newres;



}



} while(true);
```

To a seasoned developer, it is obvious that processing multiple megabytes with such a code leads to bad performance due to a lot of unnecessary allocations and ever-growing copy operations. A lot of times, such a problem is not noticed during testing but only once a certain level of concurrency is reached where the number of GCs and the amount of temporary memory is needed, it becomes a problem.

While working with large documents, it is therefore important to optimize the processing logic and prevent it from being held completely in the memory.

## Memory-related ClassLoader issues

In modern enterprise applications, the memory requirements for loaded classes can quickly amount to several hundred MB and contribute to memory problems. In the Hotspot JVM, classes are located in the permanent generation or PermGen. It represents a separate memory area, and its size must be configured separately. If this area is full, no more classes can be loaded, and an out-of-memory occurs in the PermGen. The other JVMs do not have a permanent generation, but that does not solve the problem. Class loader problems are some of the most difficult problems to detect. Most developers never have to deal with this topic and tool support is also poorest in this area. The following are some such problems:

Large classes

It is important to not increase the size of classes unnecessarily. This is especially true when classes contain a great many string constants, such as in GUI applications. Here all strings are held in constants. This is a good design approach, but it should not be forgotten that these constants also require space in the memory. In the case of the Hotspot JVM, string constants are a part of the PermGen, which can then quickly become too small.

Multiple instances of the same class in the memory

Application servers and OSGi containers have a problem with too many loaded classes and the resulting memory usage. Application servers make it possible to load different applications or parts of applications in isolation to one another. One feature is that multiple versions of the same class can be loaded to run different applications inside the same JVM. Due to incorrect configuration this can quickly double or triple the amount of memory needed for classes.

These problems can best be diagnosed with a heap dump or trending dump (jmap -histo). If a class is loaded multiple times, its instances are also counted multiple times. Thus, if the same class appears multiple times with a different number of instances, such a problem has been identified. The responsible class loader can be determined in a heap dump through simple reference tracking. The variables of the class loader reveal a reference to the application module and the .jar file. This makes it possible to determine whether the same .jar file is being loaded multiple times by different application modules.

Same class loaded repeatedly

The repeated loading of the same class does not appear to be present twice in the memory. What many forget is that classes are garbage collected too, in all three large JVMs. The Hotspot JVM does this only during a major GC, whereas both IBM and JRockit can do so during every GC. Therefore, if a class is used for only a short time, it can be removed from the memory again immediately. Loading a class is not exactly cheap and usually not optimized for concurrency. If the same class is loaded by multiple threads, Java synchronizes these threads.

In case of the Hotspot JVM, this problem will only occur under load and memory pressure as it requires a major GC, whereas in the IBM JVM or JRockit this can already happen under moderate load. The class might not even survive the first garbage collection.