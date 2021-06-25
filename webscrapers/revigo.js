const puppeteer = require("puppeteer");
const fs = require("fs");
const glob = require("glob");
const path = require("path");

async function revigo(fileName, destination) {
  const data = await fs.readFileSync(fileName, "utf8");
  const browser = await puppeteer.launch({
    headless: true,
  });
  const page = await browser.newPage();
  await page.goto("http://revigo.irb.hr/");
  const [button] = await page.$x("//button[contains(., 'Accept and Close')]");
  if (button) {
    await button.click();
  }
  await page.waitForSelector("#ctl00_MasterContent_txtGOInput");
  await page.$eval(
    "#ctl00_MasterContent_txtGOInput",
    (el, data) => (el.value = data),
    data
  );
  await page._client.send("Page.setDownloadBehavior", {
    behavior: "allow",
    downloadPath: destination,
  });
  await page.screenshot({ path: "example.png" });
  await page.click("#ctl00_MasterContent_btnStart");
  await page.screenshot({ path: "example.png" });
  await page.waitForSelector(
    "#ctl00_MasterContent_tabResults_BP_TreeMap > div > p > a:nth-child(2)"
  );
  await page.$eval(
    "#ctl00_MasterContent_tabResults_BP_TreeMap > div > p > a:nth-child(2)",
    (el) => el.click()
  );
  await page.waitForSelector(
    "#ctl00_MasterContent_tabResults_BP_TreeMap > div > p > a:nth-child(1)"
  );
  await page.$eval(
    "#ctl00_MasterContent_tabResults_BP_TreeMap > div > p > a:nth-child(1)",
    (el) => el.click()
  );
  await page.screenshot({ path: "example.png" });
  await browser.close();
}

function revigoDirectory(InputDirectory, OutpuDirectory) {
  glob(InputDirectory + "/**/*.csv", {}, (err, files) => {
    files.forEach((file) => {
      dir = path.basename(file, ".csv");
      if (!fs.existsSync(OutputDirectory + dir)) {
        fs.mkdirSync(OutpuDirectory + dir);
      }
      revigo(file, OutpuDirectory + dir);
    });
  });
}
//revigo(
// "/home/david/Documents/BenoitLab/RNA-seq/Gprofiler/downDeet.csv",
//"/home/david/Documents/BenoitLab/RNA-seq/Revigo/"
//);
revigoDirectory(
  "/home/david/Documents/BenoitLab/RNA-seq/Gprofiler/",
  "/home/david/Documents/BenoitLab/RNA-seq/Revigo/"
);
