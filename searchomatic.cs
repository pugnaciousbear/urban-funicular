using Discord;
using Discord.API;
using Discord.Logging;
using Discord.Commands;
using Discord.ETF;
using Discord.Legacy;
using Discord.Net;
using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;
using System.IO;
using Newtonsoft.Json;
using Google.Apis.Customsearch.v1;
using Google.Apis.Customsearch.v1.Data;



namespace SearchOMatic
{
    class Program
    {

        string token = "MjM5Nzk0MzA3NDkyNjEwMDQ5.Cu59ZA.qniYni2KVrisTwgIvAdGvU2K8do";
        const string apiKey = "AIzaSyC7sZwsm6KyehHNqOQEV669AG47dfVs0Fs";
        const string searchEngineId = "004183145178373012931:xbqgoq8nwlc";
        string query = null;

        static void Main(string[] args)
        {
            new Program().Start();
        }

        private DiscordClient _client;


        public void Start()
        {



            _client = new DiscordClient(x =>
            {
                x.AppName = "Search O' Matic";
                x.AppUrl = "";
                x.LogLevel = LogSeverity.Info;
                x.LogHandler = Log;
            });

            _client.UsingCommands(x =>
            {
                x.PrefixChar = 's';
                x.AllowMentionPrefix = true;
                x.HelpMode = HelpMode.Public;
            });

            CreateComamnds();
            _client.ExecuteAndWait(async () =>
            {


                _client.MessageReceived += async (s, e) =>
                {

                    if (e.Message.IsAuthor) return;


                    string spce = " ";

                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"Server: {e.Server.Name} | Channel: {e.Channel.Name} | User: {e.User} {spce}: {e.Message.Text}");
                    Console.ResetColor();
                    if (e.Message.Channel.IsPrivate)
                    {
                        Console.WriteLine("Recieved DM " + e.User.Name + e.Message.Text);
                    }
                    if (e.Message.IsMentioningMe())
                    {
                        await e.Channel.SendMessage(e.User.Mention + " yo fam whats good ma brutha type !help if you gotta get some help ma brutha");
                    }

                };


                await _client.Connect(token, TokenType.Bot);
            });


        }





        public void CreateComamnds()
        {
            var cService = _client.GetService<CommandService>();

            cService.CreateCommand("game")
               .Description("Owner Only - Sets game")
               .Parameter("game", ParameterType.Required)
               .Do(async (e) =>
               {

                   if (e.User.Id == 131182268021604352)
                   {


                       if (e.GetArg("game") != null)
                       {

                           var newgame = e.GetArg("game");
                           _client.SetGame(newgame);
                           await e.Channel.SendMessage("Game set to: " + newgame);
                       }
                       else
                       {

                           await e.Channel.SendMessage("error");
                       }
                   }

               });


            cService.CreateCommand("search")
               .Description("google search!")
               .Parameter("google", ParameterType.Required)
               .Do(async (e) =>
               {

                   if (e.GetArg("google") != null)
                   {
                       query = e.GetArg("google");
                       CustomsearchService customSearchService = new CustomsearchService(new Google.Apis.Services.BaseClientService.Initializer() { ApiKey = apiKey });
                       Google.Apis.Customsearch.v1.CseResource.ListRequest listRequest = customSearchService.Cse.List(query);
                       listRequest.Cx = searchEngineId;

                       Search search = listRequest.Execute();
                       int i = 0;
                       await e.Channel.SendMessage("Sending first 3 items!");
                       foreach (var item in search.Items)
                       {
                           if (++i == 3) break;
                           await e.Channel.SendMessage("Title : " + item.Title + Environment.NewLine + "Link : " + item.Link + Environment.NewLine + Environment.NewLine);


                       }
                       //await e.Channel.SendMessage("Game set to: " + newgame);
                   }


                   else
                   {

                       await e.Channel.SendMessage("error");
                   }


               });


            cService.CreateCommand("hello")
                          .Description("Says hello")
                          .Parameter("user", ParameterType.Required)
                          .Do(async (e) =>
                          {
                              if (e.GetArg("user") != null)
                              {
                                  //LOGIC HERE
                                  await e.Channel.SendMessage("Hello " + e.User.Name);
                              }
                              else
                              {
                                  await e.Channel.SendMessage("Error");
                              }
                          });

            cService.CreateCommand("invite")
               .Description("Lol its an invite")
               .Do(async (e) =>
               {
                   await e.Channel.SendMessage("Add our bot to your server: https://discordapp.com/oauth2/authorize?client_id=239794307492610049&scope=bot&permissions=0");
               });


            cService.CreateCommand("dnd")
             .Description("Do not disturb")
             .Do(async (e) =>
             {
                 _client.SetStatus(Discord.UserStatus.DoNotDisturb);
                 await e.Channel.SendMessage("Changed to do not disturb.");
             });

            cService.CreateCommand("online")
                .Description("online")
                .Do(async (e) =>
                {
                    _client.SetStatus(Discord.UserStatus.Online);
                    await e.Channel.SendMessage("Changed to online.");
                });


            cService.CreateCommand("idle")
                .Description("idle")
                .Do(async (e) =>
                {
                    _client.SetStatus(Discord.UserStatus.Idle);
                    await e.Channel.SendMessage("Changed to idle.");
                });

            //cService.CreateCommand("sendfile")
            //    .Description("sends a file to a channel")
            //    .Do(async (e) =>
            //    {
            //        await e.Channel.SendFile("tails.jpg");
            //        await e.Channel.SendMessage("file sent!");
            //    });


        }

        //Ｆ  Ｉ  ＲＥ  Ｓ      Ａ  Ｅ  Ｓ  Ｔ  Ｈ  Ｅ  Ｔ  Ｉ  Ｃ
        //Ｃ  Ｒ  Ａ  Ｓ  Ｈ      Ｉ  Ｓ      Ａ        Ｆ  Ａ  Ｇ  Ｇ  Ｏ  Ｔ JUST LIKE DUSKA
        //Ｖ  Ａ  Ｐ  Ｏ  Ｒ  Ｇ  Ａ  Ｙ

        public void Log(object sender, LogMessageEventArgs e)
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            if (e.Severity == LogSeverity.Warning)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
            }
            Console.WriteLine($"[{e.Severity}] [{e.Source}] [{e.Message}]");
            Console.ResetColor();



        }
    }
}
