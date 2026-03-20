import type { Product } from '../types';
import ProductCard from './ProductCard';

const ProductGrid = ({ products }: { products: Product[] }) => {
  return (
    <div>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductGrid;