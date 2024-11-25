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
extract_file_words(filepath) iterates over every line in the file, calling parse_line() on each, parse_line calls sanitize_word() on every word in each line. If there are l lines and each line has n words, the complexity of parse_line is O(l⋅n). To simplify, N can be the total number of words in the file (l⋅n), which makes the complexity of extracting the words O(N).

Although parse_line() calls sanitize_word() on each word, where O(c) is the (c is the number of characters in the word).This is not included in the overall complexity of extracting words because the growth of c does not increase in the input in N increases, hence it is left out of the equation.

complexity = O(N) where N is the total number of words in a file.
- **indexing the words:**
Forward index: O(1) as it is simply assigning a value to a key
Document rank: O(1) as it is a simple calculation for each file
Inverted index & term frequency: O(N) where N is the number of words in the file (and the max number of iterations these functions might do - within each functions the operations have O(1) complexity)

complexity after discarding constant factors = O(N)

_**overall the complexity of the indexing operation is O(N) where N is the number of words in the file**_



### Big-O complexity of a search operation:
break-down by function tasks:
- **query parsing:**
complexity = O(q), where q is the number of words in the query
- **calculating the weight multiplier of the query:**
Dictionary lookup and arithmetic have O(1) complexity but the number of lookups is determined by O(q⋅f), where q is the number of words in the query and f is the number of files in the directory

complexity = O(q⋅f)
- **calculating the result:** 
Lookup and arithmetic is O(1) but it is done f times therefore, O(1⋅f) = O(f) where f is the number of files in the directory

complexity = O(f)
- **sorting the result:** 
The .sorted() function has O(f⋅log f) complexity where f is the number of files in the result (worst case: all files are in the result).
    - further look at .sorted() function:
        This function uses the Timesort algorithm which is a hybrid merge sort and insertion sort algorithm. In the worst case, it can only use merge sort which has O(f⋅log f). 
        Merge sort essentially halves the problem size at each step (hence O(log f)), and then merges the results together (hence O(f⋅ log f)).

complexity = O(f⋅log f)

**overall:**
The complexity of the search operation without the constant factors is **O(q+ q⋅f + f + f⋅logf)**

O(q) and O(f) can be dropped from the equation as they grow at a slower rate than O(q⋅f) and O(f⋅log f).

_**Therefore, the simplified complexity of the search operation is O(q⋅f + f⋅logf).**_

### Big-O complexity of a brute force search operation: 
This would involve having to search through every word in every file for each word in the query.
**overall:**
the complexity of the search operation without the constant factors is **O(q⋅N⋅f)** , where q is the number of words in the query, N is the number of words in the file and f is the number of files in the directory.
- having N in the search complexity is likely to effect the performance significantly as in most cases, N will be the largest variable what will have to be iterated over repeatedly.


# B: Choice of Data Structures
## Your Answer
Dictionaries where chosen to store all the output file variables as they provide a lookup time of O(1). A list would have ben impractical as the search time would be O(N), where N is the number of elements in the list and would have introduced unnecessary looping nested listing to the code.
Since the nature of a search engine is to match queries to documents, it made sense to use dictionaries as they provide key-value pairs.

Lists were used to store the words in the files as they needed to be iterated over before being indexed and they also needed to be mutable for the purpose of parsing and adding the words from the each line.

The sorted_result was processed as a list of tuples (result.items()), where the tuple contained (file_name, weight). This was done so that the results could be sorted by weight of the file (handled by x: x[1] in the lambda function) and the file_name could be printed in print_result()

# C: Discuss extra features, if any:
If you implemented any extra feature on top of the requirements noted in this hanadout, briefly describe them here.

## Your Answer
n/a 
