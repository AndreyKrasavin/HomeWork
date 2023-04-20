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