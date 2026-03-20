export const api = async (url: string) => {
  try {
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
};