# week 3 - performance Notes
## Baseline performance

### Test Description

The baseline query reads the processed parquet dataset and performs:

- Filter: `country = Germany`
- Group by: `StockCode`
- Aggregation : `SUM(TOTAL_AMOUNT)`
- Sorting: descending `Total_Sales`
- No caching
- No additional repartitioning

### Baseline Result

Execution time: **0.67 seconds**

### Baseline Explain plane

The physical plan included:
- Scan parquet
- Project
- HashAggregate
- Exchange
- HashAggregate
- Exchange
- Sort
- Adaptive Spark Plan

The `Exchange` operation indicate shuffle activity during aggregation and sorting.

---

## Partition Pruning

### Test Descriotion

The same query was executed against the patitioned parquet dataset using:

`country = Germany`

### Result

Execution time: **0.88 seconds**

The execution time was slightly higher than the baseline measurement. Since both tests were executed separately on a local machine, this small difference is not sufficient to conclude that partition pruning reduced execution time.

### Explain Plan Evidence

Partition pruning was confirmed in the 'Scan parquet' operation.

The physical plan contained:

`partitionFilters: country = Germany`

This indicates that Spark can use the partition column to eliminate irrelevant partitions during the scan.

### Column Purning

The `ReadSchema` showed only the columns required by the query:

- `StockCode`
- `Total_Amount`

This indicates that Spark also applied column pruning when reading the parquet data.

### Conclusion

Partition pruning is successfully implemented and confirmed through the physical execution plan.
the execution-time difference will not be treated as performance improvement because the measurements were performed on local environment and the difference was small.

---

## Caching

### Test Description

Caching was tested by executing the same aggregation query using:

1. The original DataFrame without the same caching.
2. A cached DataFrame.
3. The cached DataFrame reused for another action.

The query filtered:

`country = Germany`

and grouped the data by:
`StockCode`

with:

`SUM(Total_Amount)`

### Results

| Test | Execution Time |
|------|---------------:|
| Without Cache |6 min 49 sec |
| With Cache | 0.54 sec |
| Reused Cache | |0.76 sec |

### Explain plan contained:

This confirms that Spark read the cached Dataframe from memory.

The plan also contained the partition filter:

`Country = Germany`

showing that the partition pruning remained avalible.

### Conclusion

Caching significantly reduced the execution time for the tested workload after the DataFrame was cached.

The main benfit of caching is expected when the same DataFrame is reused across multiple actions or queries.

---

## Repartitioning

### Test Description

Repartitioning was tested using the same aggregation query.

The query:

- filtered the data using `country = Germany`
- Grouped the data by `StockCode`
- Calculated `SUM(Total_Amount)`
- Sorted the results by `Total_Sales` in descending order.

Two tests were performed:

1. Without repartitioning 
2. With repartitioning using 8 partitions based on `StockCode`

### Results

| Test | Execution Time |
|------|----------------|
|Without Repartitioning | 6.43 seconds |
With Repartitioning | 1.0 seconds |

### optimization

The redistributed the data across 8 partitions on `StockCode`.

### Performance Improvement

The execution time decreased from 6.43 seconds to 1.o seconds.

This represents an approximately 85.2% reduction in execution time for this specific test.

### Explain Plan Evidence

The physical execution plan contained:

`Exchange hashpartitioning(StockCode,8)` 

This confirms that Spark redistributed the data based on `StockCode` across 8 partitions.

The plan also contained:

`partitionFilters: country = Germany`

This confirms that partition pruning remained available when filtering by the partition column.

The `FileScan parquet` operation showed that Spark read only the required columns:

- `StockCode`
- `Total_Amount`

### Conclusion

For this workload, repartioning by `StockCode` significantly improved the execution time of the aggregation query.

However, repartitioning introduces shuffle overhead, so it should be used when the redistribution provides a meaningful benefit for the workload.

---

## Optimization Summary

During the performance experiments, three Spark optimization techniques were evaluated:

### 1. Partition Pruning

Partition pruning was confirmed using:

`country = Germany`

The physical plan contained:

`PartitionFilters: country = Germany`

This allows Spark to avoid reading irrelevant country partitions.

The measured execution time was not lower than the baseline in this local test, so no performance improvement was claimed based on timing alone.

### 2. Caching

Caching was tested by reusing a DataFrame across multiple actions.

The physical plan contained:

`InMemoryTableScan`

This confirmed that Spark was able to read the cached DataFrame from memory.

Caching is particularly useful when the same DataFrame is reused multiple times.

### 3. Repartitioning

The DataFrame was repartitioned using:

`repartition(8, "StockCode")`

The physical plan contained:

`Exchange hashpartitioning(StockCode, 8)`

This confirmed that Spark redistributed the data across 8 partitions based on `StockCode`.

For the tested workload, execution time decreased from:

`6 min 43 sec`

to:

`1 min 00 sec`

This represents an approximately 85.1% reduction in execution time.

### Overall Conclusion

The experiments demonstrate that Spark optimization techniques have different effects depending on the workload.

Partition pruning improves data selection by reducing unnecessary partition reads.

Caching can improve repeated operations by keeping reusable data in memory.

Repartitioning can improve operations such as `groupBy` when the data is distributed appropriately, although it introduces shuffle overhead.

Performance measurements should be interpreted in the context of the execution environment and workload.
