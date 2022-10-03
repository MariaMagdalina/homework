// Данная программа из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
Console.Write("Введите количество строк: ");
int size = Convert.ToInt32(Console.ReadLine());
// объявляем массив
string[] arrString; 
arrString = new string[size];
// заполняем массив элементами
for(int i=0; i < size ; i++)
{
   Console.Write("Введите новую строку ");
   arrString[i] = Console.ReadLine();
}
// выводим массив на экран
for(int i=0; i < size ; i++)
{
   Console.WriteLine(arrString[i]);
}