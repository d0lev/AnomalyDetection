**This project was taken as part of the course:**
**Methods for detecting cyber attacks by Dr. Ran Dubin from Ariel University.**



<p align="center" width="90%">
    <img width="80%" src="https://s4.gifyu.com/images/web-gif.gif">
</p>
In this dataset, there are attacks that you will need to detect. This data is network data from physical
hosts. Can you find which hosts are anomalous/ outliers?

# Data Set

Each record has four fields (features) that are described in the dataset.

The shape of the dataset - 

```
(256670, 4)
```

------

| Features  | Description                                                  | Type    |
| --------- | ------------------------------------------------------------ | ------- |
| Record ID | Unique identifier for each connection record.                | Numeric |
| Duration  | Denotes the number of seconds (rounded) of the connection. For<br/>example, a connection for 0.17s or 0.3s would be indicated with a “0” in this field. | Numeric |
| Src_bytes | Represents the number of data bytes transferred from the source to the<br/>destination (i.e. the number of outgoing bytes from the host). | Numeric |
| Dst_bytes | Represents the number of data bytes transferred from the destination<br/>to the source (i.e. the number of bytes received by the host). | Numeric |

