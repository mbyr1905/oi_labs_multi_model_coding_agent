import type { CartItem } from '../types';

const CartItemComponent = ({ item }: { item: CartItem }) => {
  return (
    <div>
      <h2>{item.name}</h2>
      <p>{item.price}</p>
    </div>
  );
};

export default CartItemComponent;