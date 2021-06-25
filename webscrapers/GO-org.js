const puppeteer = require("puppeteer");
const fs = require("fs");
const glob = require("glob");
const path = require("path");

async function GO(data, destination) {
  const browser = await puppeteer.launch({
    headless: true,
  });
  const page = await browser.newPage();
  await page.goto("http://geneontology.org/");

  await page.waitForSelector("#landing_gene_input");
  await page.select("#rte_species", "IXOSC");
  await page.$eval(
    "#landing_gene_input",
    (el, data) => (el.value = data),
    data
  );
  const [newpage] = await Promise.all([
    new Promise((resolve) => page.once("popup", resolve)),
    page.$eval("button.btn:nth-child(2)", (el) => el.click()),
  ]);
  await page._client.send("Page.setDownloadBehavior", {
    behavior: "allow",
    downloadPath: destination,
  });
  newpage.screenshot({ path: "./example.png" });
  await newpage.waitForSelector("body > a:nth-child(3)");
  await newpage.$eval("body > a:nth-child(3)", (el) => el.click());
}
function GOdirectory(InputDirectory, OutputDirectory) {
  glob(InputDirectory + "/**/*.csv", {}, (err, files) => {
    files.forEach((file) => {
      dir = path.basename(file, ".csv");
      if (!fs.existsSync(OutputDirectory + dir)) {
        fs.mkdirSync(OutputDirectory + dir);
      }
      GO(file, OutputDirectory + dir);
    });
  });
}
GOdirectory(
  "/home/david/Documents/BenoitLab/NewBlast/Output/",
  "/home/david/Documents/BenoitLab/RNA-seq/GOorg/"
);
