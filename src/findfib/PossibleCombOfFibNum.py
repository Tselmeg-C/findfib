import math
import numpy as np

class PossibleCombOfFibNum():
    def __init__(self,target):
        self.target=target
        self.fibonacci_numbers = self.get_fib_num_under_threshold()
        self.fib_combinations_sum_to_target=[]
        #self.find_fib_combinations_sum_to_target()

    def get_fib_num_under_threshold(self):
        fibonacci_numbers = [1, 1]
        #target = 20
        i=2
        next=fibonacci_numbers[1]
        while(True):
            next = fibonacci_numbers[i-1]+fibonacci_numbers[i-2]
            if next>=self.target:
                break
            else:
                fibonacci_numbers.append(next)
                i=i+1
        return fibonacci_numbers[2:]

    def find_fib_combinations_sum_to_target(self):
        self._subset_sum(self.fibonacci_numbers,self.target)
        
    def _subset_sum(self, numbers, target, partial=[]):
        s = sum(partial)
        # check if the partial sum is equals to target
        if s == target:
            self.fib_combinations_sum_to_target.append(partial)
        if s >= target or len(numbers)==0:
            return  # if we reach the number why bother to continue

        k = numbers[0]
        repeat_num = math.floor(self.target/k)
        for i in range(repeat_num+1):
            remaining = numbers[1:]
            self._subset_sum(remaining, target, partial + [k]*i)

    def _complexity(self):
        iters =[math.ceil(self.target/i) for i in self.fibonacci_numbers]
        return np.prod(iters)




