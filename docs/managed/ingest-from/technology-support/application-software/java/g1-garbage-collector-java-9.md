---
title: G1 Garbage Collector – Java 9
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/g1-garbage-collector-java-9
---

# G1 Garbage Collector – Java 9

# G1 Garbage Collector – Java 9

* 4-min read
* Updated on May 04, 2026

Oracle’s Java 9 Hotspot VM ships with the Garbage First (G1) GC as its default garbage collector. This GC, first introduced in Java 7, can efficiently and concurrently deal with very large heaps. It can also be configured to not exceed a maximum pause time.

Most state-of-the-art GCs classify heaps into either young generation or old generation objects. This is done mostly because studies of real-world Java applications have shown that more than 90% of objects don’t survive their first garbage collection. Older objects that have survived a few collection cycles tend to remain alive and have a 98% chance of surviving. Java GCs split the young generation objects further into the survivor space and the Eden space.

Newly allocated objects are always allocated to the Eden space. Once an object survives its first garbage collection, it’s moved to the older generation. This is done so that:

* a run-time efficient algorithm can be used on new objects; the run-time depends only on the number of surviving objects but wastes half the heap size.
* a memory efficient algorithm can be used on the old generation; the run time depends on the heap size but uses the available memory as efficiently as possible.
  A heap of such a collector would look like this:

![Java heap](https://cdn.bfldr.com/B686QPH3/as/6ms8r5pq7cwh7h9q5h4fhfp/Java_Heap_Memory_Generational_Layout_-_Light_Mode?auto=webp&format=png&position=1)

Java heap

Compared to most garbage collectors, G1 has two major advantages:

* it can perform concurrently without halting application threads
* it uses non-continuous spaces which enables G1 to efficiently deal with very large heaps

Due to the way it uses the available heap, G1 can collect young and old generations simultaneously. Instead of splitting the heap into 3 spaces, Eden, survivor, and old, it splits the heap into multiple tiny regions that have the default size of 2MB. Each region is assigned to a space.

A G1 heap typically looks like this:

![Java G1 heap](https://cdn.bfldr.com/B686QPH3/as/j82pc645v8vzmcvcqhp9rw/Set_up_a_proxy_-_Java_G1_Heap_-_Light_Mode?auto=webp&format=png&position=1)

Java G1 heap

Splitting the heap into small regions enables G1 to select a small group of regions to collect and finish quickly. If a region is scheduled for collection, all surviving objects are copied from the collected region to an unassigned region. Assuming that the collected region was of the Eden space, the unassigned region holding all surviving objects become a survivor region. Ideally, if a region is full of garbage and doesn’t contain a single surviving object, it can be declared “unassigned” and has no work done on it.

To collect the entire heap, G1 can select any number or combination of regions to collect. To optimize collection time, it always selects regions that are full or almost full of garbage, thereby minimizing the amount of work needed to be done to free heap space for subsequent allocations. Other GCs always collect an entire generation, so their run-time complexity depends on the total heap size. In the case of G1, this depends on the number of live objects because the memory can be freed without handling an entire generation. Ideally, when the heap is big enough, some regions will always be completely full of garbage, making it easy to collect them.

In addition, G1 can do most of its work concurrently. In the Java world, we already know about concurrent collections from the Concurrent Mark & Sweep GC (CMS). However, the CMS can only collect the old generation concurrently and still needs to halt the application to collect the young generation. The process happens in the following phases:

1. **Initial mark**: G1 only stops the application at the beginning of garbage collection to do some quick bookkeeping before resuming the application.
2. **Concurrent mark**: While the application is executing, the GC follows all references and marks life objects.
3. **Final mark**: The application is suspended again, and a final cleanup takes place.
4. **Evacuation**: A few regions are selected and collected.

Because the **Evacuation** phase is fast, especially in the case of large heaps, G1 usually outperforms other GCs in terms of suspension time of the executed application.

The disadvantage is that G1 doesn’t perform well with small heaps, so consider the application in question. If required, you can always go back to the default collector by setting the `-XX:+UseParallelOldGC` flag. If the G1 has very little heap available, you will see **Full GCs** in the GC log. A **Full GC** is only performed when G1 determines that the usual mode of operation is no longer possible. In this case, the entire heap is collected with a slow, but memory-efficient algorithm that makes things better for the next collection. If there are only full GCs, you could consider increasing the heap size and opting for a different GC.

Due to the small regions, G1 can be configured to limit its maximum pause time by setting `-XX:MaxGCPauseMillis=n`. G1 will then consider the previous collections and the amount of detected garbage before estimating the maximum number of regions it can collect at once without overstepping this limit.

G1 is still far from being a real-time collector, but performs marginally better than other collectors that are limited in their rigid heap structures.