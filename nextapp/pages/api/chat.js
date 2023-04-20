export default async function (req, res) {

  const response = await fetch(process.env.LCC_ENDPOINT_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      
    },
    body: JSON.stringify({
      message: req.body.message,
    }),//history: req.body.history
  });

    const data = await response.json();

    res.status(200).json({ result: data })
}