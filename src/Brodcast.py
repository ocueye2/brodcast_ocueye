import threading

bcfunct = {}  # Stores registered functions
threads = []  # Stores running threads

class brodcast:
    @staticmethod
    def cont(name):
        if name not in bcfunct:
            raise Exception("No registered function found for: " + name) 
        
        tempthreads = []
        for item in bcfunct[name]:
            tempthreads.append(threading.Thread(target=item))  # Corrected function call
        
        for thread in tempthreads:
            thread.start()
            threads.append(thread)  # Store thread in global list


    @staticmethod
    def wait(name):
        if name not in bcfunct:
            raise Exception("No registered function found for: " + name) 
        
        tempthreads = []
        for item in bcfunct[name]:
            tempthreads.append(threading.Thread(target=item))  # Corrected function call
        
        for thread in tempthreads:
            thread.start()
        for thread in tempthreads:
            thread.join()


    @staticmethod
    def debug():
        print("\nRegistered Functions:", bcfunct)

    @staticmethod
    def on(receve):
        if receve not in bcfunct:
            bcfunct[receve] = []  # Initialize list if key doesn't exist

        def funct(func):
            bcfunct[receve].append(func)  # Store function
            return func  # Return func to make it a proper decorator

        return funct  # Return the decorator function
