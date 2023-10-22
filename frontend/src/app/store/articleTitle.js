// Пример!!!

import { createSlice } from '@reduxjs/toolkit';

const articleTitleSlice = createSlice({
  name: 'articleTitle',
  initialState: '',
  reducers: {
    setArticleTitle: (state, action) => action.payload,
  },
});

export const { setArticleTitle } = articleTitleSlice.actions;
export default articleTitleSlice.reducer;
