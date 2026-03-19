interface CartItemProps {
  item: {
    id: number;
    name: string;
    price: number;
    quantity: number;
  };
}

const CartItem = ({ item }: CartItemProps) => {
  return (
    <div>
      <h2>{item.name}</h2>
      <p>Price: {item.price}</p>
      <p>Quantity: {item.quantity}</p>
    </div>
  );
};

export default CartItem;