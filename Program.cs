// Данная программа из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
Console.Write("Введите количество строк: ");
int size = Convert.ToInt32(Console.ReadLine());
// объявляем массив
string[] arrString, arrNewString; 
arrString = new string[size];
arrNewString = new string[size];

// заполняем массив элементами
for(int i=0; i < size ; i++)
{
   Console.Write("Введите новую строку ");
   arrString[i] = Console.ReadLine();
}

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
for(int i=0; i < j ; i++)
{
   Console.WriteLine(arrNewString[i]);
}