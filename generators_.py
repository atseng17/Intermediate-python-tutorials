learning_iterator=False
learning_generator=True
EXAMPLE=True
VERBOSE=False
if learning_iterator:
    if VERBOSE:
        """
        One can loop over any iterables, such as lists, tuples, dicts, strings, files, generators.
        Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
        Any object that have __iter__() method is an iterable, just check `dir(iterable)`

        An iterator is an object with a 'state' that remembers the state of the iterable, and knows what the next value to retrieve by the __next__ method
        """
        mytuple = ("apple", "banana", "cherry")
        print(dir(mytuple))
        myit = iter(mytuple)
        print(dir(myit))
        print(next(myit))
        print(next(myit))
        print(next(myit))
        print('======')

        # so how do we know when the iterator should stop? this is what we can do
        myit = iter(mytuple)
        while True:
            try:
                item = next(myit)
                print(item)
            except StopIteration:
                print("======")
                break

        # The for loop actually creates an iterator object and executes the next() method for each loop.
        # so this is actually looping through a iterator
        # for x in mytuple:
        #   print(x)
        """
        # what's running under the hood of the "for loop"?
        # create an iterator object from that iterable
        iter_obj = iter(iterable)

        # infinite loop
        while True:
            try:
                # get the next item
                element = next(iter_obj)
                # do something with element
            except StopIteration:
                # if StopIteration is raised, break from loop
                break
        """

        # now create an iterator class
        class PowTwo:
            """Class to implement an iterator
            of powers of two"""

            def __init__(self, max=0):
                self.max = max
            # __iter__() returns an iterable object
            # if we dont have this method, then we cant use "iter()" on it
            # which leads to TypeError: iteration over non-sequence
            def __iter__(self):
                self.n = 0
                return self

            def __next__(self):
                if self.n <= self.max:
                    result = 2 ** self.n
                    self.n += 1
                    return result
                else:
                    raise StopIteration
        numbers = PowTwo(3)
        i = iter(numbers)

        # Using next to get to the next iterator element
        print(next(i))
        print(next(i))
        print(next(i))
        print(next(i))
        print('======')

        # now create an iterator class that does not stop at all
        class InfIter:
            """Infinite iterator to return all
                odd numbers"""
            def __iter__(self):
                self.num = 1
                return self

            def __next__(self):
                num = self.num
                self.num += 2
                return num

        numbers_inf = InfIter()# create an object
        i = iter(numbers_inf)# create an iterable from the object
        print(next(i))
        print(next(i))
        print('======')
    if EXAMPLE:
        """Write a iterator what prints out a range between 1 to 10"""
        print("solution 1: using an iterator class")
        class range_iter:
            def __init__(self,start,end):
                self.count = start
                self.end = end
            def __iter__(self):
                return self
            def __next__(self):
                if self.count>=self.end:
                    raise StopIteration
                current = self.count
                self.count+=1
                return current
        
        riter = range_iter(1,10)
        for item in riter:
            print(item)
        
        print("solution 2: using generator")
        def range_gen(start,end):
            current = start
            while current<end:
                yield current
                current+=1
        geniter = range_gen(1,10)
        for i in geniter:
            print(i)

        """write an iterator that splits sentences"""
        class sentence_spliter:
            def __init__(self,sentence):
                self.counter = 0
                self.words = sentence.split()
                self.sentence = sentence
            def __iter__(self):
                return self
            def __next__(self):
                if self.counter>=len(self.words):
                    raise StopIteration
                currentindex = self.counter
                self.counter+=1
                return self.words[currentindex]
        
        my_sentence = sentence_spliter("Hi, I love dogs")
        for word in my_sentence:
            print(word)

if learning_generator:
    if VERBOSE:
        # A simple generator function
        def my_gen():
            n = 1
            print('This is printed first')
            yield n

            n += 1
            print('This is printed second')
            yield n

            n += 1
            print('This is printed at last')
            yield n

        a = my_gen()
        # The next() function returns the next item in an iterator.
        next(a) 
        next(a)
        next(a)

        # Using for loop to replace manually next
        for item in my_gen():
            pass

    if EXAMPLE:
        """write a fuction that outputs all prime numbers smaller that
        a given maximum number"""
        # using traditional way
        def list_all_prime(max_num):
            prime_list=[]
            def check_if_prime(num):
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        return False
                return num

            for num in range(2,max_num):
                prime = check_if_prime(num)
                if prime:
                    prime_list.append(prime)
            return prime_list

        print(list_all_prime(49))

        # using a iterator
        def check_if_prime(num):
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        return False
                return True
        class list_all_prime_iter:
            def __init__(self, max_num):
                self.max = max_num
                self.count = 1
            def __iter__(self):
                return self
            def __next__(self):
                self.count += 1        
                if self.count >= self.max:            
                    raise StopIteration        
                elif check_if_prime(self.count):            
                    return self.count        
                else:   # when check_if_prime is false
                    return self.__next__()
        prime_list = iter(list_all_prime_iter(32))
        for i in prime_list:
            print(i)

        # using a generator
        def check_if_prime(num):
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        return False
                return True
        def list_all_prime_gen(num):
            for i_ in range(2,num):
                if check_if_prime(i_):
                    yield i_
        prime_list = iter(list_all_prime_gen(32))
        for i in prime_list:
            print(i)
        # or
        prime_list = ( i_ for i_ in range(2,32) if check_if_prime(i_))
        for i in prime_list:
            print(i)
        

        """write an iterator that splits sentences"""
        def sentence_spliter(sentence):
            for words in sentence.split():
                yield words
        
        my_sentence = sentence_spliter("Hi, I love dogs")
        for word in my_sentence:
            print(word)


        def rev_str(my_str):
            length = len(my_str)
            for i in range(length - 1, -1, -1):
                yield my_str[i]
        for char in rev_str("hello"):
            print(char)


        class PowTwo:
            def __init__(self, max=0):
                self.n = 0
                self.max = max

            def __iter__(self):
                return self

            def __next__(self):
                if self.n >= self.max:
                    raise StopIteration

                result = 2 ** self.n
                self.n += 1
                return result

        def PowTwoGen(max=0):
            n = 0
            while n < max:
                yield 2 ** n
                n += 1

        powiter = PowTwo(10)
        powgen = PowTwoGen(10)
        for i in powiter:
            print(i)
        for i in powgen:
            print(i)
        # print(next(powergen))

