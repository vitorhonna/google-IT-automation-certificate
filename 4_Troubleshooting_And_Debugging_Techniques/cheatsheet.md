# Useful commands

## Show ongoing network connections to analyze traffic
- tcpdump
- Wireshark

## Show number and types of resources used in the system
- ps
- top
- free

## Show system and library calls made by a program
- strace
- ltrace

## Show which processes are using the most input and output
- iotop

## Show statistics on the input/output and virtual memory operations
- iostat
- vmstat

## Make a system reduce its priority to access the disk
- ionice

## Show the current traffic on the network interfaces
- iftop

## Option to limit the bandwidth
- rsync (used for backing up data) -bwlimit
- Trickle

## Reduce the priority of a process in accessing the CPU
- nice

## Apache benchmark tool
- ab 
- Ex: `ab -n 500 site.example.com/` average time of 500 requests

## Change the priority of a group of tasks that are already running
- `for pid in $(pidof <task_name>); do renice <priority> $pid; done`
- The priorities range from 0 (highest) to 19 (lowest)
- `pidof` gets the list of pids
- `renice` changes the priority

## To figure out how a process got started
- `ps ax` shows all the running processes on the computer
- Pipe the results to `less` to be able to scroll through the results: `ps ax | less`
- `\` is the search key when using `less`

## Look for files in the hard drive
- `locate <filename>`

## Stop processes without cancelling them completely
- `killall -STOP <process_name>`

## Restart processes one after the other, not in parallel, checking every second for completion.
- Here, the condition is met as long as the process exists, and fail when it goes away (then it moves onto the next task)
- `for pid in $(pidof <task_name>); do while kill -CONT $pid; do sleep 1; done; done`

## Measure a script speed
- `time <script>`, returns 3 values:
  - "Real": amount of actual time that it took to execute the command (wall-clock time)
  - "User": time spent doing operations in the user space
  - "Sys": time spent doing system-level operations

## Python profiler: pprofile3
- `pprofile3 -f callgrind -o profile.out <script>` uses the "callgrind" file format and stores the output in the "profile.out" file

## Graphical interface to look into the files
- `kcachegrind <filename.out>`

## Test the health of the RAM
- `memtest86`

## Information about network connections
- `netstat` gets information depending on the flags passed:
  - `-n` numerical addresses instead of resolving host names
  - `-l` only check sockets that are listening for connection
  - `-p` print the process ID and name to which each socket belongs

## Check memory leaks
- `valgrind` (linux / mac) for C/C++
- Dr. Memory (windows / linux)

## Python interactive debugger
- `pdb3 <program.py + parameters>`
- use `next` to run the next line
- use `continue` to run the program until it continues or crashes
- use `print(<variable>)` to print
- 

## Python module to enable/disable printing debug messages
- `logging`

## Generate Core files (store all the information related to the crash so it can be debugged)
- `ulimit -c unlimited` 

## Debugger
- `gdb -c core <executable>` (core is the Core file created with ulimit)
- `backtrace` command, show the functions call history (how the program reached the failed state)
- use `up` to access the previous functions
- use `list` to show the lines around the current line
- use `print <variable>` to print


