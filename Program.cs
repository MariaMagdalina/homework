// Данная программа из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам.

void fill_array(string [] arr) // функция заполнения массива элементами
{
  for(int i=0; i < arr.Length ; i++)
   {
      Console.Write("Введите строку " + i + " : ");
      arr[i] = Console.ReadLine();
   } 
} 

 int q_string(string arr) // функция подсчета количества символов в строке
 { 
   int quantity = 0; // переменная для подсчета символов в строке
   foreach(var ch in arr)
   {
      quantity++;
   }
   return quantity;
 }

// основная программа
Console.Clear();
Console.Write("Введите количество строк: ");
int size = Convert.ToInt32(Console.ReadLine());
// объявляем массивы
string[] arrString, arrNewString; 
arrString = new string[size];
arrNewString = new string[size];
fill_array(arrString); // заполняем массив 
int j = 0; // индекс для нового массива
for(int i=0; i < size ; i++) // заполняем новый массив элементами в соответствии с условием задания
{
   if(q_string(arrString[i]) <= 3) // если количество символов <=3 записываем элемент в новый массив
     {
       arrNewString[j] = arrString[i];
       j++;
     } 
}
// выводим новый массив
Console.WriteLine();
Console.WriteLine("Новый массив:");
for(int i=0; i < j ; i++)
{
   Console.WriteLine(arrNewString[i]);
}