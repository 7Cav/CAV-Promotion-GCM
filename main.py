import sys
import Promotions
import GC_ADM


"""
Main function to run the program. Required Inputs:
    :arg Task to Perform
"""
if __name__ == '__main__':
    if len(sys.argv) > 1:
        task_to_do = sys.argv[1]
        if task_to_do == 'Create Promotion Citations':
            Promotions.process()
        elif task_to_do == 'GC and ADM':
            GC_ADM.process()
        else:
            raise Exception('Unknown task: {0}'.format(task_to_do))
    else:
        raise Exception('The minimal input is a task to perform!')
