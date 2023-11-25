### README for `string_sifter.py`

#### Description
String Sifter is a Python tool designed for memory analysis, particularly focusing on identifying processes associated with specific memory addresses and strings. It is especially useful in contexts such as debugging, forensic analysis, or detecting memory leaks in systems. The tool reads a list of memory addresses and scans the memory maps of all running processes to find those containing these addresses.

#### Features
- Process Identification: Identifies processes that have memory regions containing specified addresses.
- Memory Address Mapping: Maps each process ID (PID) to a list of matching memory addresses.
- Efficient Scanning: Optimized to handle large sets of addresses and numerous processes.

#### Requirements
- Operating System: Linux-based system (with memprocfs support).
- Python Version: (specify Python version here, e.g., Python 3.8 or newer).

#### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Dreksis/string_sifter.git
   ```
2. Navigate to the cloned directory:
   ```
   cd string_sifter
   ```

#### Usage
To use `string_sifter.py`:
- Prepare a text file containing memory addresses in hexadecimal format, each on a new line.
- Specify the path to the memprocfs root directory.
- Run the script with the following command:
```
python string_sifter.py [result_file_path] [memprocfs_root]
```
- `result_file_path`: Path to a file containing memory addresses.
- `memprocfs_root`: Path to the memprocfs root directory.

#### License
This project is licensed under the [MIT License](LICENSE.md).

---

