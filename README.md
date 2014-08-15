python_gil_demonstration
========================

Python's default interpreter can run a single thread per virtual core due to Global Interpreter Lock implementation. This code demonstrates CPU usage while running a busy wait function using 8 threads and 8 processes.

Tests are run on an system with i5 processor (i5-4250U), which has 2 cores and 4 virtual cores (hyperthreading?). Output below indicates interpreter does not employ second physical core when using threads. But when using processes both cores are working with 100% utilization.

    before starting threads (idle)
    [4.9, 3.0, 2.1, 2.0]
    [3.1, 6.0, 3.1, 5.9]
    [5.0, 3.0, 3.0, 5.9]
    [6.9, 4.0, 2.0, 6.9]
    [5.9, 3.0, 7.0, 2.0]
    [8.0, 5.9, 3.0, 2.0]
    [7.0, 4.0, 2.1, 2.0]
    [5.9, 4.0, 3.1, 2.0]
    [8.0, 5.1, 4.0, 2.0]
    [2.0, 3.0, 5.0, 2.9]
    starting threads
    done
    threads running
    [61.4, 62.1, 53.6, 55.2]
    [59.8, 59.5, 56.5, 58.1]
    [60.2, 59.1, 56.0, 53.4]
    [58.8, 60.4, 54.0, 55.7]
    [65.3, 58.8, 56.7, 57.8]
    [60.2, 62.4, 58.0, 56.7]
    [63.3, 60.4, 55.1, 54.1]
    [59.8, 59.3, 56.0, 55.6]
    [62.2, 61.8, 55.7, 54.0]
    [58.8, 60.4, 54.0, 57.9]
    after threads stopped (idle)
    [6.9, 4.0, 2.0, 3.0]
    [5.0, 5.0, 0.0, 5.0]
    [4.0, 5.0, 2.0, 3.0]
    [2.0, 4.0, 1.0, 4.0]
    [3.0, 6.8, 3.0, 5.0]
    [5.9, 8.0, 3.1, 4.9]
    [7.0, 3.0, 2.0, 4.9]
    [7.9, 3.0, 2.0, 2.0]
    [2.0, 4.0, 2.0, 4.9]
    [5.9, 5.0, 5.2, 4.0]
    starting processes
    done
    processes running
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
    [100.0, 100.0, 100.0, 100.0]
