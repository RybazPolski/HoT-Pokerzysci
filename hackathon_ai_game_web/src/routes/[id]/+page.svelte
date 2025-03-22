<script lang="ts">
    import type { PageProps } from './$types';
    import Window from "$lib/components/Window.svelte";

    let { data }: PageProps = $props();

    console.log(data)

</script>


<div class="flex w-screen mt-10">

    <div class="w-2/12"></div>

    <div class="w-8/12">
        <div class="text-2xl mb-5">NPC Parameters</div>

        <Window>
            <div class="w-full h-full">
                <div class="grid grid-cols-2 grid-rows-2 gap-4 mt-5">
                    <div>
                        <p>Here you can adjust selected NPC's settings </p>
                    </div>
                    <div class="flex flex-col gap-1">
                        <label for="npc_name">NPC name: </label>
                        <input type="text" id="npc_name"
                               class="border border-gray-300 rounded-md p-1 indent-2 transition duration-300"
                               placeholder="f. e. Spongebob"
                        />
                    </div>
                </div>
            </div>
        </Window>
    </div>

    <div class="w-2/12"></div>


</div>