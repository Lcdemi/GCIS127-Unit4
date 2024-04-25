import sorts
import time
import list_utils
import random
import plotter

SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def insertion_sort_function_timer(a_list):
    start = time.perf_counter()
    sorts.insertion_sort(a_list)
    end = time.perf_counter()
    return end - start

def merge_sort_function_timer(a_list):
    start = time.perf_counter()
    sorts.merge_sort(a_list)
    end = time.perf_counter()
    return end - start

def sort_function_timer(sort_function, a_list):
    start = time.perf_counter()
    if sort_function == sorts.quick_insertion_sort:
        sort_function(a_list, len(a_list))
    else:
        sort_function(a_list)
    end = time.perf_counter()
    return end - start

def plot_sort_time_using_random_lists(sort_function):
    print("timing", sort_function.__name__)
    plotter.new_series(sort_function.__name__)
    for value in SIZES:
        sizes_array = []
        for _ in range(value):
            randvalue = random.randint(0, value)
            sizes_array.append(randvalue)
        plotter.add_data_point(sort_function_timer(sort_function, sizes_array))
    return plotter

def plot_sort_time_using_sorted_lists(sort_function):
    print("timing", sort_function.__name__)
    plotter.new_series(sort_function.__name__)
    for value in SIZES:
        sizes_array = []
        for i in range(value):
            sizes_array.append(i)
        plotter.add_data_point(sort_function_timer(sort_function, sizes_array))
    return plotter

def main():
    plotter.init("Random Lists", "", "Time") #quick_insertion_sort is the quickest sorting method for random lists
    plot_sort_time_using_random_lists(sorts.insertion_sort)
    plot_sort_time_using_random_lists(sorts.merge_sort)
    #plot_sort_time_using_random_lists(sorts.quicksort)
    plot_sort_time_using_random_lists(sorts.quick_insertion_sort)
    plotter.plot()

    plotter.init("Sorted Lists", "", "Time") #insertion sort is the quickest sorting method for sorted lists
    plot_sort_time_using_sorted_lists(sorts.insertion_sort)
    plot_sort_time_using_sorted_lists(sorts.merge_sort)
    #plot_sort_time_using_sorted_lists(sorts.quicksort) #quicksort does not work (error) because it reaches the recursion limit (over 1000 iterations)
    plot_sort_time_using_sorted_lists(sorts.quick_insertion_sort)
    plotter.plot()


    #random.seed(1)
    #sorted_list = list(range(5000))
    #print("Sorted:", insertion_sort_function_timer(sorted_list))
          
    #random_list = list_utils.random_list(5000)
    #print("Random:", insertion_sort_function_timer(random_list))

    #reverse_list = list(range(4999, -1, -1))
    #print("Reversed:", insertion_sort_function_timer(reverse_list))

    #a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    #b_list = [8, 7, 6, 5, 4, 3, 2, 1]
    #print("Time:", sort_function_timer(sorts.merge_sort, b_list))
    #print("Time:", sort_function_timer(sorts.insertion_sort, b_list))
    #print("Sorted:", merge_sort_function_timer(a_list))
    #print("Reversed:", merge_sort_function_timer(b_list))

if __name__ == "__main__":
    main()

   # [1, 2, 3, 4, 5, 6, 7, 8]    [8, 7, 6, 5, 4, 3, 2, 1]
   # [1, 2, 3, 4][5, 6, 7, 8]    [8, 7, 6, 5][4, 3, 2, 1]
   # [1, 2][3, 4][5, 6][7, 8]    [8, 7][6, 5][4, 3][2, 1]
   # [1][2][3][4][5][6][7][8]    [8][7][6][5][4][3][2][1]
   # [1, 2][3, 4][5, 6][7, 8]    [8, 7][6, 5][4, 3][2, 1]
   # [1, 2, 3, 4][5, 6, 7, 8]    [8, 7, 6, 5][4, 3, 2, 1]
   # [1, 2, 3, 4, 5, 6, 7, 8]    [8, 7, 6, 5, 4, 3, 2, 1]
