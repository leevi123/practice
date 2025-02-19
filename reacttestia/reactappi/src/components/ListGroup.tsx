import { useState } from "react";

// https://www.youtube.com/watch?v=SqcY0GlETPk&t=163s 50:48

function ListGroup() {
  let items = ["finland", "sweden", "russia", "norway", "denmark"];
  const [selectedIndex, setSelectedIndex] = useState(-1);

  return (
    <>
      <h1>List</h1>
      {items.length === 0 && <p>item not found</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            onClick={() => {
              // sets selectedIndex to a new value of (index) and rerenders the page
              setSelectedIndex(index);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
