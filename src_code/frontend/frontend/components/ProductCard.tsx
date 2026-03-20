import type { Product } from '../types';

const ProductCard = ({ product }: { product: Product }) => {
  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>{product.price}</p>
    </div>
  );
};

export default ProductCard;