function App() {
  const names: Array<string> = [
    "Nikita",
    "Denis",
    "Egor",
    "Trofim huesos",
    "Karim huesos",
  ];
  const ages: Array<number> = [17, 15, 14, 13, 12, 8];

  const getRandomName = () => Math.floor(Math.random() * names.length);
  const getRandomAge = () => Math.floor(Math.random() * ages.length);

  return (
    <>
      <h1 className="some">Name: {names[getRandomName()]}</h1>
      <h1 className="some">Age: {ages[getRandomAge()]}</h1>
    </>
  );
}

export default App;
