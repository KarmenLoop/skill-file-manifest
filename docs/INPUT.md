# Input and output

Supply a UTF-8 JSON object (maximum 10 MiB). Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| root | Local directory path. |
| paths | Nonempty array of relative file paths under root; no symlink components. |

## Example

```json
{
  "root": "examples/files",
  "paths": [
    "brief.txt",
    "copy.txt"
  ]
}
```

## Result

files with path, bytes and sha256; total_bytes; duplicate_groups of relative paths.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
