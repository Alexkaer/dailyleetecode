"""
地址：https://leetcode.com/problems/min-stack/description/
描述：
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

思路：
我们每次入栈的时候，保存的不再是真正的数字，而是它与当前最小值的差（当前元素没有入栈的时候的最小值）。 这样我们pop和top的时候拿到栈顶元素再加上上一个最小值即可。 另外我们在push和pop的时候去更新min，这样getMin的时候就简单了，直接返回min。

注意上面加粗的“上一个”，不是“当前的最小值”

经过上面的分析，问题的关键转化为“如果求的上一个最小值”，解决这个的关键点在于利用min。

pop或者top的时候：

如果栈顶元素小于0，说明栈顶是当前最小的元素，它出栈会对min造成影响，我们需要去更新min。 上一个最小的是“min - 栈顶元素”,我们需要将上一个最小值更新为当前的最小值
因为栈顶元素入栈的时候的通过 栈顶元素 = 真实值 - 上一个最小的元素 得到的， 而真实值 = min， 因此可以得出上一个最小的元素 = 真实值 -栈顶元素

如果栈顶元素大于0，说明它对最小值没有影响，上一个最小值就是上上个最小值。

关键点：
最小栈存储的不应该是真实值，而是真实值和min的差值
top的时候涉及到对数据的还原，这里千万注意是上一个最小值
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, x):
        if len(self.stack) == 0:
            self.min = x
            self.stack.append(0)
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        if len(self.stack) == 0:
            return
        else:
            v = self.stack.pop()
            if v < 0:
                self.min = self.min - v

    def top(self):
        top = self.stack[-1]
        if top < 0:
            return self.min
        else:
            return self.min + top

    def get_min(self):
        return self.min


obj = MinStack()
obj.push(1)
obj.push(2)
obj.top()
obj.get_min()
obj.pop()
obj.get_min()
obj.top()
