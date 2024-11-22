*The PA Directory Search Engine*

Practical Algorithms 2024-25, University of Glasgow
Assessed Exercise 1

Submitted by: 
(If applicable,) project was done in partnership with: 

# A: Complexity Analysis
Present the following complexity analysis in this report:

+ Big-O complexity of the indexing operation.
+ Big-O complexity of a search operation (given that indexing has been done already).
+ Big-O complexity of a search operation if it were implemented in a brute force fashion (that is, no indexing performed, all search queries go through the entire text of all files every time).

You should be very clear about what you mean by n when presenting your Big-O complexity analysis.

_Note_: You don’t have to do a line-by-line code-analysis like we do in certain other problems. Instead, present your analysis as a text description that walks through the relevant operations, comments on their complexity with rationale, and then presents the overall complexity.

## Your Answer

### Big-O complexity of the indexing operation:
break-down by function tasks:
- **read all files in the directory and extracting the words:**
extract_file_words() on the surface has O(l) complexity, where l is the number lines in the file but internally, this function calls parse_line() which also has O(n) complexity where n is the number of words in each line. the amount of work done by this function is determined by the number of words in the file. so the complexity of this function is O(n)
- **indexing the words:**
forward index: O(n) where n is the number of words in the file
document rank: O(1) for each file
inverted index: O(n) where n is the number of words in the file
term frequency: O(n) where n is the number of words in the file

_**overall the complexity of the indexing operation is O(n) where n is the number of words in the file**_



### Big-O complexity of a search operation:
break-down by function tasks:
- **query parsing:**
O(q) where q is the number of words in the query
- **calculating the weight multiplier of the query:**
dictionary lookup is O(1) but the number of lookups is determined by O(q . f), where q is the number of words in the query anf f is the number of files in the directory
- **calculating the result:** 
the lookup is O(1) but it is done f times therefore, O(1 . f) = O(f) where f is the number of files in the directory
- **sorting the result:** 
the .sorted() function has O(f log f) complexity where f is the number of files in the result
    - further look at .sorted() function:
        this function uses the Timsort algorithm which is a hybrid merge sort and insertion sort algorithm. In the worst case, it can only use merge sort which has O(f . log f). 
        Merge sort essentially halves the problem size at each step (hence O(log f)), and then merges the results together (hence O(f)).

**overall:**
the complexity of the search operation without the constant factors is **O(q + q . f + f + f . log f)**
- Simplified Worst-Case Complexity
Dominant Terms: 
    - O(k⋅n) (query checks across all documents)
    - O(n . log n) (sorting results).

_**Therefore, the simplified complexity of the search operation is O(k ⋅ n + n . log n).**_

### Big-O complexity of a brute force search operation: 


# B: Choice of Data Structures
Explain and justify your choice of data structures.

## Your Answer
...


# C: Discuss extra features, if any:
If you implemented any extra feature on top of the requirements noted in this hanadout, briefly describe them here.

## Your Answer
...
