import { createClient } from '@supabase/supabase-js'

const url: string = import.meta.env.VITE_SUPABASE_URL ?? "";
const key: string = import.meta.env.VITE_SUPABASE_API_KEY ?? "";



// Create a single supabase client for interacting with your database
export const supabase = createClient(url, key);