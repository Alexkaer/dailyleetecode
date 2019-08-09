"""
地址：https://leetcode-cn.com/problems/implement-queue-using-stacks/

描述：
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

思路：
这道题目是让我们用栈来模拟实现队列。 我们直到栈和队列都是一种受限的数据结构。 栈的特点是只能在一端进行所有操作，队列的特点是只能在一端入队，另一端出队。

在这里我们可以借助另外一个栈，也就是说用两个栈来实现队列的效果。这种做法的时间复杂度和空间复杂度都是O(n)。

由于栈只能操作一端，因此我们peek或者pop的时候也只去操作顶部元素，要达到目的 我们需要在push的时候将队头的元素放到栈顶即可。

因此我们只需要在push的时候，用一下辅助栈即可。 具体做法是先将栈清空并依次放到另一个辅助栈中，辅助栈中的元素再次放回栈中，最后将新的元素push进去即可。
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        global front
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        front = self.stack2.pop()
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        return front

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack1:
            return self.stack1[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0
