<script lang="ts">

import Window from "$lib/components/Window.svelte";
import Datatable from "$lib/components/Datatable.svelte";
import {onMount} from "svelte";

let agents = $state();
let titles = ["Name", "Created At", "Status", "Traits"];

onMount(async ()=>{
    agents = [
        {
            name: "Spongebob",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Happy"
        },
        {
            name: "Spongebob",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Happy"
        },
        {
            name: "Spongebob",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Happy"
        },
        {
            name: "Spongebob",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Happy"
        },
        {
            name: "Spongebob",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Happy"
        },
        {
            name: "Patrick",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Dumb"
        },
        {
            name: "Squidward",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Grumpy"
        },
        {
            name: "Mr. Krabs",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Greedy"
        },
        {
            name: "Plankton",
            created_at: "2021-10-10",
            status: "Active",
            traits: "Evil"
        }
    ]
})

</script>


<div class="flex w-screen bg-custom_white-500 mt-10 mb-10">

    <div class="w-2/12"></div>

    <div class="w-8/12">
        <div class="text-2xl mb-5">List of AI Agents/NPC</div>

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