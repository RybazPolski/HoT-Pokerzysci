<script lang="ts">
import {supabase} from "$lib/helper/supabase";
import Window from "$lib/components/Window.svelte";
import Datatable from "$lib/components/Datatable.svelte";
import {onMount} from "svelte";

let agents = $state();
let titles = ["Name", "Created At", "Traits"];

onMount(async ()=>{

    let { data: npc, error } = await supabase
        .from('npc')
        .select('*')

    console.log(npc);

    agents = [

    ]
})

</script>


<div class="flex w-screen bg-custom_white-500 mt-10 mb-10">

    <div class="w-2/12"></div>

    <div class="w-8/12 relative">
        <div class="text-2xl mb-5">List of AI Agents/NPC</div>
        <a href="/game" class="bg-green-500 transition cursor-pointer p-1 px-2 rounded text-white-600 border-1 border-gray-500 absolute top-0 right-40 hover:bg-green-600">Start Playing</a>
        <a href="/create" class="bg-white cursor-pointer p-1 rounded text-slate-600 border-1 border-gray-500 absolute top-0 right-0">Add new agent</a>
        <Window>
            {#if agents && Array.isArray(agents) && agents.length > 0}
                <Datatable agents={agents} titles={titles} />

                {:else}
                Loading...

            {/if}
        </Window>
    </div>

    <div class="w-2/12"></div>


</div>