import type { Category } from '../types';

const CategorySidebar = ({ categories }: { categories: Category[] }) => {
  return (
    <div>
      <h2>Categories</h2>
      <ul>
        {categories.map((category) => (
          <li key={category.id}>{category.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default CategorySidebar;