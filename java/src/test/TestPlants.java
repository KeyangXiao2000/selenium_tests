package test_plants;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.Duration;
import java.util.List;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestPlants {

	WebDriver driver;

	@BeforeEach
	public void chromeSetup() {
		driver = new ChromeDriver();

        driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));
		driver.get("https://keyangxiao2000.github.io/coursera-react-final-project/");
	}

	@Test
	public void testTitles() {

		String title = driver.getTitle();
		assertEquals("E-Plant", title, "Site name error");

		List<WebElement> categories = driver.findElements(By.cssSelector(".product-grid > div"));
		assertEquals(categories.size(), 5, "Product grid size error");
		assertEquals(categories.get(0).findElement(By.cssSelector("h1")).getAttribute("innerHTML"), "Air Purifying Plants", "Air purifying plants name error");

		List<WebElement> lmps = categories.get(4).findElements(By.cssSelector(".product-card"));
		assertEquals(lmps.size(), 6, "Low maintenance plants size error");

		WebElement zz = lmps.get(0).findElement(By.cssSelector(".product-title"));
		assertEquals(zz.getAttribute("innerHTML"), "ZZ-Plant", "ZZ plant name error");

	}

	@AfterEach
	public void teardown() {
		driver.quit();
	}

}
