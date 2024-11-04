def merge(left, right):
    while left and right:
        if left[0] <= right[0]:
            yield left.pop(0)
        else:
            yield right.pop(0)
    while left:
        yield left.pop(0)
    while right:
        yield right.pop(0)

def merge_sort(lista):
    if len(lista) <= 1:
        yield lista
    else:
        middle = len(lista) // 2
        left = lista[:middle]
        right = lista[middle:]
        
        left = list(merge_sort(left))[0]
        right = list(merge_sort(right))[0]
        
        sorted_list = list(merge(left, right))
        yield sorted_list

def iterator_sort(lista):
    for sorted_list in merge_sort(lista):
        for i in sorted_list:
            yield i

def main():
	lista = [1, 8, 3, 2, 1, 3, 15, 2, 0]

	for x in iterator_sort(lista):
		print(x, end = " ")
	print("\n")

	# 0 1 1 2 2 3 3 8 15 

if __name__ == "__main__":
	main()