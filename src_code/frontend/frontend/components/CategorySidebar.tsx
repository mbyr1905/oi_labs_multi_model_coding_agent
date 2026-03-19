import Link from 'next/link';

const CategorySidebar = () => {
  return (
    <div>
      <h2>Categories</h2>
      <ul>
        <li>
          <Link href="/category/electronics">Electronics</Link>
        </li>
        <li>
          <Link href="/category/clothing">Clothing</Link>
        </li>
      </ul>
    </div>
  );
};

export default CategorySidebar;