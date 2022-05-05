#class _Accumulator:
    #so_far = 0

    #def __call__(self, args):
    #   self.so_far += args
    #   return self.so_far

#def make_accumulate():
    #   return _Accumulator()
 
#acc = make_accumulate()

def make_accumulate():
    current = 0
    def accumulate(arg):
        nonlocal current
        current += arg
        return current
    return accumulate

acc = make_accumulate()
