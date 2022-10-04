// Данная программа из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам.
// функция заполнения массива элементами
void fill_array(string [] arr)
{
  for(int i=0; i < arr.Length ; i++)
   {
      Console.Write("Введите новую строку ");
      arr[i] = Console.ReadLine();
   } 
} 

// основная программа
Console.Clear();
Console.Write("Введите количество строк: ");
int size = Convert.ToInt32(Console.ReadLine());
// объявляем массивы
string[] arrString, arrNewString; 
arrString = new string[size];
arrNewString = new string[size];
fill_array(arrString);

// подсчитываем количество символов в строках
 int j = 0; // индекс для нового массива
for(int i=0; i < size ; i++)
{
   int quantity = 0; // переменная для подсчета символов в строке
  
   foreach(var ch in arrString[i] )
   {
      quantity++;
   }
   if(quantity <= 3) // если количество символов <=3 записываем элемент в новый массив
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