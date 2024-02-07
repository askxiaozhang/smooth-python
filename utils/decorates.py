from loguru import logger
import functools

def timer_decorator(func, cur_evaluating= set()):
    import time
    @functools.wraps(func)
    def warpper(*args, **kwargs):
        if func not in cur_evaluating:
            cur_evaluating.add(func)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.info(f"func name: {func.__name__} Time elapsed: , {end - start:.4f}" )
            cur_evaluating.remove(func)
        else:
            result = func(*args, **kwargs)

        return result

    return warpper

if __name__ == "__main__":
    @timer_decorator
    def main():
        print("6")

    main()