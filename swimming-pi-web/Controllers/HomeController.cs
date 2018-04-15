using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using swimming_pi_web.Models;

namespace swimming_pi_web.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            var results = TempData["results"] as IEnumerable<SensorReading>;

            return View(results);
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        [HttpPost("UploadFiles")]
        public async Task<IActionResult> Post()
        {
            List<SensorReading> readings = new List<SensorReading>();

            var files = Request.Form.Files;

            foreach (var file in files)
            {
                var filePath = Path.GetTempFileName();

                try
                {
                    using (var stream = new FileStream(filePath, FileMode.Create))
                    {
                        await file.CopyToAsync(stream);
                    }
                    if (file.ContentType == "text/plain")
                    {
                        readings.AddRange(Services.SensorLog.Process(filePath));
                    }
                }
                catch
                {
                }
            }

            return Ok(Json(readings));
        }
    }
}
