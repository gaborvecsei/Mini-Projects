/******************************************

Created By Vecsei Gábor
Blog: https://gaborvecsei.wordpress.com/
Email: vecseigabor.x@gmail.com
https://bitbucket.org/gaborvecsei/

******************************************/

using System;
using System.Text.RegularExpressions;

namespace PhoneNumberFinder
{
    class Program
    {
        public static void FindPhoneNumbers(string text)
        {
            //Find phone numbers with this format: +36 (1) 123 1234
            const string phone_regex = @"\+\d{2}\s\(\d{1,2}\)\s\d{3}\-\d{4}";
            Regex rx = new Regex(phone_regex, RegexOptions.Compiled | RegexOptions.IgnoreCase);
            // Find the matches
            MatchCollection matches = rx.Matches(text);
            //Write the phone numbers to the console
            foreach (Match match in matches)
            {
                Console.WriteLine(match.Value.ToString());
            }
        }
        static void Main(string[] args)
        {
            //Get data from a website
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString("https://www.aut.bme.hu/Staff");
            //Find the numbers
            FindPhoneNumbers(webData);
            Console.ReadKey();
        }
    }
}