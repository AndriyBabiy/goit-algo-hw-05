In exercise 03.py, the goal was to analyse and assess the speed of execution of search algorithms. The algorithms assessed were the Knuth Morris Pratt, Rabin Karpp, and Boyer Moore search algorithms.

Based on running the searching algorithms on two txt documents that were both greater than 10,000 characters in length each, the following table of results was achieved:

  ./стаття_1.txt                                                                                                   
  ----------------------------------------------------------------------------------------------------------------  
| Word                 | Location             | KnuthMorrisPratt     | RabinKarp            | BoyerMoore           |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| Література           | 11480                | 0.0052435            | 0.0048522            | 0.0045239            |
| Літератураа          | -1                   | 0.0045099            | 0.0044522            | 0.0043096            |
| Автори публiкації    | 56                   | 0.0043949            | 0.0046766            | 0.0044756            |
| https://dou.ua/      | 12000                | 0.0042597            | 0.0044974            | 0.0044853            |
| AMD Ryzen 5 3600     | -1                   | 0.0043874            | 0.0042723            | 0.0045041            |

  ./стаття_2.txt                                                                                                    
  ----------------------------------------------------------------------------------------------------------------  
| Word                 | Location             | KnuthMorrisPratt     | RabinKarp            | BoyerMoore           |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| Література           | 15561                | 0.004786             | 0.00444              | 0.0049133            |
| Літератураа          | -1                   | 0.0046163            | 0.0045665            | 0.004527             |
| Автори публiкації    | 94                   | 0.004331             | 0.0046487            | 0.0044022            |
| https://dou.ua/      | -1                   | 0.0043666            | 0.0042399            | 0.0043243            |
| AMD Ryzen 5 3600     | 9704                 | 0.0042926            | 0.0043698            | 0.0042749            |

From the tables of results we can see that the overall performance of each algorithm is quite comprable as all of them seem to execute the searches in around 0.005 seconds. The speed of locating strings that are in the text were often slower than the identification that a string was missing from the text corpus. These cases of missing strings are identifiable by the -1 in the location column.
