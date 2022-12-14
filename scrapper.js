function scrapeWebsite(url) {
    // Use the fetch API to get the HTML from the website
    fetch(url)
      .then(response => response.text())
      .then(html => {
        // Parse the HTML into a DOM tree
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
  
        // Use the querySelectorAll() method to get all the elements with a specific class
        const elements = doc.querySelectorAll(".some-class");
  
        // Loop through the elements and do something with them (e.g. extract data)
        elements.forEach(element => {
          // Extract the data from the element (e.g. text content)
          const data = element.textContent;
  
          // Do something with the data (e.g. log it to the console)
          console.log(data);
        });
      });
  }