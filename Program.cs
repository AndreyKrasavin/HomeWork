// Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
Console.WriteLine("введите два числа");
int num1 = Convert.ToInt32(Console.ReadLine());
int num2 = Convert.ToInt32(Console.ReadLine());
if (num1 > num2)
{
    System.Console.WriteLine($" {num1} больше {num2}");
}
if (num1 < num2)
{
    System.Console.WriteLine($" {num2} больше {num1}");
}

//Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

Console.WriteLine("введите три числа");
int num1 = Convert.ToInt32(Console.ReadLine());
int num2 = Convert.ToInt32(Console.ReadLine());
int num3 = Convert.ToInt32(Console.ReadLine());
if (num1 > num2 && num1 > num3)
{
    Console.WriteLine($"максимальное число {num1}");
}
if (num2 > num1 && num2 > num3)
{
    Console.WriteLine($"максимальное число {num2}");
}
if (num3 > num2 && num3 > num1)
{
    Console.WriteLine($"максимальное число {num3}");
}

//Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).

Console.WriteLine("введите числo");
int num1 = Convert.ToInt32(Console.ReadLine());
if (num1 % 2 == 0)
{
    Console.WriteLine($"Число {num1} четное");
}
Console.WriteLine($"Число {num1} нечетное");

// Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

Console.WriteLine("введите числo");
int num1 = Convert.ToInt32(Console.ReadLine());
int count = 0;
while (count <= num1)
{
    System.Console.WriteLine($"{count}");
    count++;
}
