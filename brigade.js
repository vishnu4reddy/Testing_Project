const { events, Job } = require("brigadier");

events.on("push", (e, p) => {
  var test = new Job("python-tests", "python:3.9");

  test.tasks = [
    "pip install pytest",
    "pip install -r requirements.txt || true",  // if you have one
    "pytest tests/"
  ];

  test.run();
});
