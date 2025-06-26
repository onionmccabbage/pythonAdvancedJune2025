# NB async is not the same as threading
import timeit
import asyncio # be careful - this is only in recent python versions

# we must declare a function as 'async' in order to run is asynchronously
async def main():
    '''we may run any async funtion asynchronously'''
    await asyncio.sleep(1) # here would be our long-running functionality
    print('all done')

if __name__ == '__main__':
    # asyncio.run( main() )
    # we may run severla instances of our async function
    s = timeit.default_timer()
    with asyncio.Runner() as runner:
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
        runner.run(main())
    print(f'total execution: {timeit.default_timer()-s}')