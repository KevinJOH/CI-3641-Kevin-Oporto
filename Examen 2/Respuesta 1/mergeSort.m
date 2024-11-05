% Respuesta 1.b.ii
% Algoritmo mergesort

function sorted_array = merge_sort(array)
  if length(array) <= 1
    sorted_array = array;
  else
    mid = floor(length(array) / 2);
    left = merge_sort(array(1:mid));
    right = merge_sort(array(mid+1:end));
    sorted_array = merge(left, right);
  end
end

function result = merge(left, right)
  result = [];
  while ~isempty(left) && ~isempty(right)
    if left(1) <= right(1)
      result = [result, left(1)];
      left(1) = [];
    else
      result = [result, right(1)];
      right(1) = [];
    end
  end
  result = [result, left, right];
end

array = [1, 3, 15, 2, 1, 0, 8, 3];
sorted_array = merge_sort(array);
disp(sorted_array);
