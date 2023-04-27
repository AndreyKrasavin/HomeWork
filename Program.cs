// 1.  ***** Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.*****

System.Console.WriteLine($"Введите число");
int number = Convert.ToInt32(Console.ReadLine()); 
if ((number % 10) == (number / 10000) && ((number % 100) / 10) == ((number / 1000) % 10))
{
    System.Console.WriteLine($"число {number} является палиндромом");
}

else System.Console.WriteLine($"число {number} не является палиндромом");

// 2. ******Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве. ******

int x1 = Coordinate("x", "A");
int y1 = Coordinate("y", "A");
int z1 = Coordinate("z", "A");
int x2 = Coordinate("x", "B");
int y2 = Coordinate("y", "B");
int z2 = Coordinate("z", "B");

int Coordinate(string coorName, string pointName)
{
    Console.Write($"Введите координату {coorName} точки {pointName}: ");
    return Convert.ToInt16(Console.ReadLine());
}

double Decision(double x1, double x2, 
                double y1, double y2, 
                double z1, double z2){
  return Math.Sqrt(Math.Pow((x2-x1), 2) + 
                   Math.Pow((y2-y1), 2) + 
                   Math.Pow((z2-z1), 2));
}

double segmentLength =  Math.Round (Decision(x1, x2, y1, y2, z1, z2), 2 );
Console.WriteLine($"Длина отрезка  {segmentLength}");

//*******3.Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.******

System.Console.WriteLine($"Введите число ");
int countnumber = Convert.ToInt32(Console.ReadLine()); 


void Fun( int number)
{
    int i = 1;
    while(i<= number)
    {
        System.Console.WriteLine($"{i} -> {i*i*i}");
        i++;
    }
}    

Fun(countnumber)
