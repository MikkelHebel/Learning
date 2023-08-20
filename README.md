# Learning
This is a repository where I save and document stuff I'm learning about programming.


## Big O Notation
Big O tells how good a given algorithm performs when more inputs are being given.
This is told by the **Time Complexity** (How much time the alogorithm uses) and **Space Complexity** (How much space in memory the alogorithm uses).
It is great to see how slow an algorithm will get when more and more complexity is added.

**n = input total**
> n is a variable and it refers to the amount of inputs given to an algorithm.
> e.g. If an algorithm is going through an array of 5 elements, n would be 5. So it would look like this: O(5^2)

[![Big O Notation](https://miro.medium.com/v2/resize:fit:720/format:webp/1*tcC9J7lblKpkIcKzd63EdQ.png "Big O Notation")](https://miro.medium.com/v2/resize:fit:720/format:webp/1*tcC9J7lblKpkIcKzd63EdQ.png)

The picture above shows how good / bad different O Notations are and how the processing times goes up / down.
A function that grows alot when the number of inputs grows is bad, but if the function grows less that is good.
2 algorithms can have the same Big O but perform wildly different.

**Example of some Big O Notation from best to worst:**

**O(1)**
> Is the lowest O Notation and it basically means that no matter how many inputs you give it the run time will be constant.
> e.g. This is realisticly only a simple operation like "Return the first item in the list".

**O(n)**
> Many common algorithms have a Big O of n, which is linear and means the run time will be linear with the number of inputs.
> e.g. The algorithm goes through a list to find a number. The longer the list the longer the operation time.

**O(n^2)**
> Means the processing time goes up with the square of the number of inputs.
> e.g. Double the number of inputs the run time will quadruple.